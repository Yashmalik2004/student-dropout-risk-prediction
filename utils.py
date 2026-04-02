import logging

# Configure logging
def setup_logging(log_file='app.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Example utility function
def example_utility_function():
    logging.info('Example utility function called')
    # Add your utility code here
