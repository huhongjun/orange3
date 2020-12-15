import numpy as np
from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable


def series2descriptor(d):
    if d.dtype is np.dtype("float") or d.dtype is np.dtype("int"):
        return ContinuousVariable(str(d.name))
    else:
        t = d.unique()
        t.sort()
        return DiscreteVariable(str(d.name), list(t.astype("str")))

def df2domain(df):
    featurelist = [series2descriptor(df.iloc[:,col]) for col in range(len(df.columns))]
    return Domain(featurelist)

def df2table(df):
    tdomain = df2domain(df)
    ttables = [series2table(df.iloc[:,i], tdomain[i]) for i in range(len(df.columns))]
    ttables = np.array(ttables).reshape((len(df.columns),-1)).transpose()
    return Table(tdomain , ttables)

def series2table(series, variable):
    if series.dtype is np.dtype("int") or series.dtype is np.dtype("float"):
        series = series.values[:, np.newaxis]
        return Table(series)
    else:
        series = series.astype('category').cat.codes.reshape((-1,1))
        return Table(series)
def column2df(col):
    if type(col.domain[0]) is Orange.feature.Continuous:
        return (col.domain[0].name, pd.Series(col.to_numpy()[0].flatten()))
    else:
        tmp = pd.Series(np.array(list(col)).flatten())  # type(tmp) -> np.array( dtype=list (Orange.data.Value) )
        tmp = tmp.apply(lambda x: str(x[0]))
        return (col.domain[0].name, tmp)

def table2df(tab):
    # Orange.data.Table().to_numpy() cannot handle strings
    # So we must build the array column by column,
    # When it comes to strings, python list is used
    series = [column2df(tab.select(i)) for i in xrange(len(tab.domain))]
    series_name = [i[0] for i in series]  # To keep the order of variables unchanged
    series_data = dict(series)
    print series_data
    return pd.DataFrame(series_data, columns=series_name)