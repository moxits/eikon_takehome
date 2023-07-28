import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine


def load_csv_data():
    users = pd.read_csv('data/users.csv')
    user_experiments = pd.read_csv('data/user_experiments.csv', sep='\t')
    user_experiments.columns = ['experiment_id', 'user_id', 'experiment_compound_ids', 'experiment_run_time']
    compounds = pd.read_csv('data/compounds.csv')
    
    return users, user_experiments, compounds   

def derive_features(user_df, experiment_df, compound_df):
    # Convert experiment_compound_ids to list of compounds for each experiment
    experiment_df['experiment_compound_ids'] = experiment_df['experiment_compound_ids'].str.replace(',', '')
    experiment_df['experiment_compound_ids'] = experiment_df['experiment_compound_ids'].apply(lambda x: list(map(int, x.split(';'))))
    
    # Explode the dataframe to get one row per compound per experiment
    experiment_df = experiment_df.explode('experiment_compound_ids')
    
    # Calculate total experiments per user
    total_experiments = experiment_df.groupby('user_id').size()/2
    
    # Calculate average experiment run time per user
    average_experiments = experiment_df.groupby('user_id')['experiment_run_time'].mean()
    
    # Calculate most common compound per user
    most_common_compound = experiment_df.groupby('user_id')['experiment_compound_ids'].agg(lambda x: x.value_counts().idxmax())
    
    # Merge all series into a single dataframe
    features_df = pd.concat([total_experiments, average_experiments, most_common_compound], axis=1)
    features_df.columns = ['total_experiments', 'average_experiments', 'most_common_compound']
    
    # Reset index to make user_id a column
    features_df.reset_index(inplace=True)
    features_df['user_id'] = features_df['user_id'].str.replace(',', '')
    features_df['user_id'] = features_df['user_id'].astype(int)
    features_df['total_experiments'].astype(int)
    
    return features_df


def df_to_sql(df,table_name):
    engine = create_engine('postgresql://postgres:postgres@db:5432/test_db')
    # Write DataFrame to SQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)


def main():
    users, user_experiments, compounds = load_csv_data()
    final_df = derive_features(users, user_experiments, compounds)
    df_to_sql(final_df,"results")
    
if __name__ == "__main__":
    main()