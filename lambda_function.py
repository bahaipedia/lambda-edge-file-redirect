def lambda_handler(event, context):
    response = event['Records'][0]['cf']['response']
    request = event['Records'][0]['cf']['request']

    '''
    This function updates the HTTP status code in the response to 302, to redirect to another
    path (cache behavior) that has a different origin configured.
    '''

    # Convert status to int for comparison
    current_status = int(response['status'])

    if 400 <= current_status <= 599:        
        print(f"Redirecting URI: {request['uri']}")
        
        # UPDATED: Use f-string for cleaner formatting
        redirect_path = f"https://bahaimedia.s3.us-east-1.amazonaws.com{request['uri']}"
        print(redirect_path)

        response['status'] = '302' # CloudFront expects status as a string
        response['statusDescription'] = 'Found'

        # Drop the body as it is not required for redirects
        response['body'] = ''
        
        # UPDATED: Safely handle headers dictionary
        # CloudFront requires lowercase keys for the headers dictionary
        if 'headers' not in response:
            response['headers'] = {}
            
        response['headers']['location'] = [{'key': 'Location', 'value': redirect_path}] 

    return response
