import yaml

if __name__ == "__main__":
    
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    data_path = config['data_path']
    results_path = config['results_path']
    plots_path = config['plots_path']

    # print(data_path, results_path, plots_path)