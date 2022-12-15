import pandas as pd
import os


class graduate_admission():

    def __init__(self, file_path) -> None:
        super().__init__()
        assert isinstance(file_path, str)
        self.file_names = os.listdir(file_path)

        # files = []
        # for f in self.file_names:
        #     files.append(pd.read_csv(os.path.join(file_path,f)))
        df1 = pd.read_csv(os.path.join(file_path, self.file_names[0]))
        df2 = pd.read_csv(os.path.join(file_path, self.file_names[1]))

        self.full_df = df1.append(df2, ignore_index=True)
        #self.full_df.drop(["Serial No."], axis=1)



if __name__ == "__main__":
    ga = graduate_admission("data/")
