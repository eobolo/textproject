import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-08-23-00-33-08-810"  # Replace with your actual endpoint name

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])  # Decode the base64-encoded image data

    # Instantiate a Predictor
    predictor = sagemaker.predictor.Predictor(
        ENDPOINT,
        sagemaker_session=sagemaker.Session(),
    )

    # For this model, the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")

    # Make a prediction
    inferences = predictor.predict(image)  # Use the decoded image data

    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
