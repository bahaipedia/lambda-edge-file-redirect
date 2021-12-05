# lambda-edge-file-redirect
If a file cannot be located, redirect user to the primary s3 bucket as a last ditch effort to find it

See also: repository lambda-edge-bahaimedia

This function captures edge cases between how we route traffic (latency-based) and how we route file requests (geographically).
