import yaml
import os

if __name__ == "__main__":
    
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    data_path = config['data_path']
    results_path = config['results_path']
    plots_path = config['plots_path']

    # print(data_path, results_path, plots_path)

    os.makedirs(os.path.join(results_path, 'trade_books'), exist_ok=True)
    os.makedirs(os.path.join(results_path, 'reports'), exist_ok=True)

    # STEP 1: READ THE DATA