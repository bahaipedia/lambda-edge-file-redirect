# lambda-edge-file-redirect
If a file cannot be located, redirect user to the primary s3 bucket as a last ditch effort to find it

See also: repository lambda-edge-detect-origin

This function captures edge cases between how we route traffic (latency) and how we route file requests (geographically). 
We have servers and s3 buckets together in the same region so this function should not be triggered that often. It could be invoked
in the unlikely event that a user uploaded a file on the US server/s3 bucket and a user in a different region requested that file
before lambda-bahaimedia-distribute-s3 had a chance to distribute it. It could also be invoked if a file uploaded (server determined) 
was directed to one region, while the file download (lambda determined) went to a different region. We assume if the file didn't
go to the users primary region, it must have ended up in the US region. 

This would also trigger if we setup a server but not a corresponding s3 bucket/cloudfront origin. A user who was generating page thumbnails on the fly 
would find that their thumbnails failed to load, because they were being generated in the US s3 bucket, but requeted in an overseas bucket, 
and always before lambda-bahaimedia-distribute had a chance to distribute them. Upon refreshing the page the file would load, but this 
script captures the request, sends it to the US s3 bucket and prevents the file not found error from happening. 

See also: lambda-bahaimedia-distribute-s3 for another example of how this function may be triggered.
