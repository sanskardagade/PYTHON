import logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level = logging.DEBUG,                  ##when you are changing the mode you need to restart the kernel 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True
)
