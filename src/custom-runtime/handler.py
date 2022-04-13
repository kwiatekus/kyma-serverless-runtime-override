import os
def main(event, context):
    print(os.environ['foo'])
    return os.environ['foo']