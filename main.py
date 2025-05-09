from nhldata import moneypuck
import pandas as pd

def get_data():
    mp_conn = moneypuck.Connector()

    shots = mp_conn.shots_season(
        season = 2024
    )

    shots_df = pd.DataFrame(shots)
    return shots_df.columns

if __name__ == '__main__':
    print(get_data())


