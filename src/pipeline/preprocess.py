import argparse
import logging 

import pandas as pd 

logging.basicConfig(
    level=logging.INFO,
     format="%(asctime)s [%(levelname)s] %(message)s"
 )

logger = logging.getLogger("preprocess")

NUMERIC_COLS = [ 
    "sepal length (cm)",
    "sepal width (cm)",  
    "petal length (cm)",
    "petal width (cm)",
]

def preprocess(input_path: str, output_path: str) ->pd.DataFrame:
    df = pd.read_csv(input_path)  

    initial_rows = len(df) 

    df = df.drop_duplicates() 

    logger.info(
        "Dropped %d duplicate rows", 
        initial_rows - len(df)
    )  

    for col in NUMERIC_COLS:    
        df[col] = pd.to_numeric(df[col], errors="coerce") 

        n_missing = df[col].isna().sum()   

        if n_missing > 0:  
            median_val = df[col].median() 
            df[col] = df[col].fillna(median_val)

            logger.info(
                "Imputed %d missing values in '%s' with median=%.3f", 
                n_missing,
                col,
                median_val
            )

    df = df.dropna(subset=["species"])

    
    # Create sepal area
    df["sepal_area"] = (
        df["sepal length (cm)"] *
        df["sepal width (cm)"]
    )

    # Create petal area
    df["petal_area"] = (
        df["petal length (cm)"] *
        df["petal width (cm)"]
    )
    

    df["sepal_to_petal_length_ratio"] = (
        df["sepal length (cm)"] /
        df["petal length (cm)"]
    )

    # Create petal length category
    df["petal_length_bin"] = pd.cut(
        df["petal length (cm)"],
        bins=[-float("inf"), 2, 5, float("inf")],
        labels=["short", "medium", "long"]
    )

    # Remove unnecessary column if it exists
    df.drop(
        columns=["collected_at"],
        inplace=True,
        errors="ignore"
    )

    # Save processed data
    df.to_csv(output_path, index=False)

    logger.info(
        "Preprocessed %d rows -> %s",
        len(df),
        output_path
    )

    return df


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="data/raw/iris_raw.csv"
    )

    parser.add_argument(
        "--output",
        default="data/processed/iris_preprocessed.csv"
    )

    args = parser.parse_args()

    preprocess(args.input, args.output)


if __name__ == "__main__":
    main()





     


