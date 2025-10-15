"""
Tool - Custom Lambda Tool
Description: fdger

IMPORTANT: Only edit the code in the main() function below.
The Lambda handler will be automatically appended during deployment.
DO NOT add lambda_handler code here - it will be added automatically.
"""

def main(event_body):
    """
    Main function for Tool
    This function will be called by the Lambda handler.
    
    Parameters:
    event_body: dict - The request body passed to the Lambda function
    
    Returns:
    dict - JSON-serializable response
    """
    # Your tool logic here
    # Access parameters from event_body
    # Example: user_input = event_body.get('input_data', '')
    
    return {
        "success": True,
        "message": "Hello from Tool!",
        "data": event_body
    }

# You can add helper functions below
