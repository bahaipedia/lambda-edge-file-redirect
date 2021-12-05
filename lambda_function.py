def lambda_handler(event, context):
    response = event['Records'][0]['cf']['response']
    request = event['Records'][0]['cf']['request']

    '''
    This function updates the HTTP status code in the response to 302, to redirect to another
    path (cache behavior) that has a different origin configured. Note the following:
    1. The function is triggered in an origin response
    2. The response status from the origin server is an error status code (4xx or 5xx)
    '''

    if int(response['status']) >= 400 and int(response['status']) <= 599:        
        print(request['uri'])
        redirect_path = 'https://bahaimedia.s3.us-east-1.amazonaws.com%s' % request['uri']
        print(redirect_path)

        response['status'] = 302
        response['statusDescription'] = 'Found'

        # Drop the body as it is not required for redirects
        response['body'] = ''   
        response['headers']['location'] = [{'key': 'Location', 'value': redirect_path}] 

    return response 
