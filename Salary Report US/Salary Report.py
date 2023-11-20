#IMPORTS
import pandas as pd
import lxml

# Main dataframe to collect data
table_from_html = pd.read_html("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
df = table_from_html[0].copy()

df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]

# Adding tables from other pages to the main dataframe
for page_no in range(1, 10):
    table_from_html = pd.read_html(
        f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_no}")
    page_df = table_from_html[0].copy()
    page_df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
    #df = df.append(page_df, ignore_index=True)  deprecatted
    df = pd.concat([df,page_df],axis=0,ignore_index=True)  #concat obj iterável

# Filtering selected columns
df = df[["Major", "EarlyCareerPay", "MidCareerPay"]]
print(df)

# Cleaning columns
df.replace({"^Major:": "", "^Early Career Pay:\$": "", "^Mid-Career Pay:\$": "", ",": ""}, regex=True, inplace=True)

# Change datatype of numeric columns
df[["EarlyCareerPay", "MidCareerPay"]] = df[["EarlyCareerPay", "MidCareerPay"]].apply(pd.to_numeric)


# print(df.nlargest(5,"EarlyCareerPay")) TOP 5