pipeline {
  agent any

  options {
    buildDiscarder(logRotator(numToKeepStr: '20'))
    disableConcurrentBuilds()
    timestamps()
  }

  environment {
    AWS_REGION = 'us-east-1'
    TF_ROOT = 'infra/terraform/environments/dev'
    IMAGE_NAME = 'campuspulse-dev'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'git rev-parse --short=12 HEAD > .image-tag'
      }
    }

    stage('Test image') {
      steps {
        sh '''
          set -eu
          IMAGE_TAG="$(cat .image-tag)"
          docker build --target test --tag "campuspulse-test:${IMAGE_TAG}" .
          docker run --rm -e PYTHONPATH=/workspace \
            -v "$PWD:/workspace" -w /workspace "campuspulse-test:${IMAGE_TAG}" \
            pytest -q --cov=/workspace/app --cov-report=xml:coverage.xml \
              --cov-fail-under=90 --junitxml=test-results.xml
        '''
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'test-results.xml'
          archiveArtifacts allowEmptyArchive: true, artifacts: 'coverage.xml'
        }
      }
    }

    stage('Lint and security') {
      steps {
        sh '''
          set -eu
          IMAGE_TAG="$(cat .image-tag)"
          docker run --rm -v "$PWD:/workspace" -w /workspace "campuspulse-test:${IMAGE_TAG}" ruff check .
          docker run --rm -v "$PWD:/workspace" -w /workspace "campuspulse-test:${IMAGE_TAG}" bandit -q -r app
          docker run --rm "campuspulse-test:${IMAGE_TAG}" pip-audit
        '''
      }
    }

    stage('Terraform checks') {
      steps {
        sh '''
          set -eu
          docker run --rm -v "$PWD:/workspace" -w "/workspace/${TF_ROOT}" \
            hashicorp/terraform:1.14.8 fmt -check -recursive
          docker run --rm -v "$PWD:/workspace" -w "/workspace/${TF_ROOT}" \
            hashicorp/terraform:1.14.8 init -backend=false
          docker run --rm -v "$PWD:/workspace" -w "/workspace/${TF_ROOT}" \
            hashicorp/terraform:1.14.8 validate
        '''
      }
    }

    stage('Build runtime image') {
      steps {
        sh '''
          set -eu
          IMAGE_TAG="$(cat .image-tag)"
          docker build --target runtime \
            --tag "${IMAGE_NAME}:${IMAGE_TAG}" \
            --tag "${IMAGE_NAME}:latest" .
        '''
      }
    }

    stage('Publish to ECR') {
      when {
        anyOf {
          branch 'develop'
          branch 'main'
        }
      }
      steps {
        sh '''
          set -eu
          IMAGE_TAG="$(cat .image-tag)"
          ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
          REGISTRY="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
          aws ecr get-login-password --region "${AWS_REGION}" | \
            docker login --username AWS --password-stdin "${REGISTRY}"
          docker tag "${IMAGE_NAME}:${IMAGE_TAG}" "${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
          if aws ecr describe-images --repository-name "${IMAGE_NAME}" \
            --image-ids "imageTag=${IMAGE_TAG}" >/dev/null 2>&1; then
            echo "Image ${IMAGE_TAG} already exists; immutable tag will be reused."
          else
            docker push "${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
          fi
        '''
      }
    }

    stage('Deploy development') {
      when {
        branch 'develop'
      }
      steps {
        dir("${TF_ROOT}") {
          sh '''
            set -eu
            IMAGE_TAG="$(cat ../../../../.image-tag)"
            terraform apply -auto-approve \
              -var="enable_runtime=true" \
              -var="image_tag=${IMAGE_TAG}"
            terraform output -raw application_url > ../../../../.application-url
          '''
        }
        sh './scripts/smoke_test.sh "$(cat .application-url)"'
      }
    }

    stage('Production approval') {
      when {
        branch 'main'
      }
      input {
        message 'Promote this immutable image to the portfolio production demo?'
        ok 'Deploy'
      }
      steps {
        echo 'Production promotion is intentionally added in Phase 6.'
      }
    }
  }

  post {
    always {
      sh 'docker image prune --force || true'
      archiveArtifacts allowEmptyArchive: true, artifacts: '.image-tag,.application-url'
    }
  }
}
