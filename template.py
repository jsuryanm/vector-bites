import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s]: %(message)s")

project_name = "src"

list_of_files = [
    
    f"{project_name}/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logger.py",
    f"{project_name}/shared_functions.py",
    f"{project_name}/interactive_search.py",
    f"{project_name}/advanced_search.py",
    f"{project_name}/enhanced_rag_chatbot.py",
    f"{project_name}/system_comparision.py",
    f"{project_name}/calorie_checker.py",
    f"{project_name}/result_limiter.py",
    "requirements.txt",
    "research/trials.ipynb",
    "streamlit_app.py",
    ".env"
]

for file_path in list_of_files:
    file_path =  Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating an empty file: {file_path}")
    
    else:
        logging.info(f"{file_name} already exists")


