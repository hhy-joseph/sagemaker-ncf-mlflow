
import pandas as pd
import numpy as np
import json
import os
import ast
from sklearn.model_selection import train_test_split

def validate_data(df):
    """Validate input data structure and types."""
    required_columns = [
        'Tourist ID', 'Age', 'Interests', 'Preferred Tour Duration',
        'Accessibility', 'Site Name', 'Sites Visited', 'Tour Duration',
        'Tourist Rating', 'Satisfaction'
    ]
    
    # Check for required columns
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    # Validate data types
    assert df['Tourist ID'].dtype in ['int64', 'int32'], "Tourist ID must be integer"
    assert df['Age'].dtype in ['int64', 'int32', 'float64'], "Age must be numeric"
    
    return True

def clean_data(df):
    """Clean and preprocess the data."""
    # Create a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Convert string lists to actual lists
    df_clean['Interests'] = df_clean['Interests'].apply(ast.literal_eval)
    df_clean['Sites Visited'] = df_clean['Sites Visited'].apply(ast.literal_eval)
    
    # Handle missing values
    df_clean['Age'].fillna(df_clean['Age'].median(), inplace=True)
    df_clean['Tourist Rating'].fillna(df_clean['Tourist Rating'].mean(), inplace=True)
    
    # Remove duplicates
    df_clean.drop_duplicates(subset=['Tourist ID', 'Site Name'], inplace=True)
    
    return df_clean

def engineer_features(df):
    """Create new features for the model."""
    df_featured = df.copy()
    
    # Create interest count feature
    df_featured['Interest_Count'] = df_featured['Interests'].apply(len)
    
    # Create previous sites count
    df_featured['Previous_Sites_Count'] = df_featured['Sites Visited'].apply(len)
    
    # Calculate tour duration difference
    df_featured['Duration_Difference'] = \
        df_featured['Tour Duration'] - df_featured['Preferred Tour Duration']
    
    # One-hot encode interests
    all_interests = set()
    for interests in df_featured['Interests']:
        all_interests.update(interests)
    
    for interest in all_interests:
        df_featured[f'Interest_{interest}'] = \
            df_featured['Interests'].apply(lambda x: 1 if interest in x else 0)
    
    return df_featured

def main():
    # Read input data
    base_dir = "/opt/ml/processing"
    input_data_path =  f"{base_dir}/input/tourism_dataset_5000.csv"
    df = pd.read_csv(input_data_path)
    
    # Validate data
    validate_data(df)
    
    # Clean data
    df_clean = clean_data(df)
    
    # Engineer features
    df_featured = engineer_features(df_clean)
    
    # Split data
    train_data, test_data = train_test_split(
        df_featured, test_size=0.2, random_state=42
    )
    if not os.path.exists(f'{base_dir}/train/'):
        os.makedirs(f'{base_dir}/train')
    if not os.path.exists(f'{base_dir}/test/'):
        os.makedirs(f'{base_dir}/test')
    # Save processed datasets
    train_data.to_csv(f'{base_dir}/train/train.csv', header=False, index=False)
    test_data.to_csv(f'{base_dir}/test/test.csv', header=False, index=False)
    print('Saving Done')
if __name__ == "__main__":
    import os 
    path = "/opt/ml/processing/input"
    dirs = os.listdir( path )
    for file in dirs:
        print(file)
    main()
