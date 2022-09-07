import baseten, truss
import os


def deploy():
    api_key = os.getenv('BASETEN_API_KEY')
    path = os.path.abspath(os.path.join('.', 'test_truss'))
    baseten.login(api_key)  # https://docs.baseten.co/settings/api-keys
    truss_handle = truss.from_directory('test_truss')
    baseten.deploy_truss(
        truss_handle,
        model_name='test_truss',
    )

if __name__ == '__main__':
    deploy()