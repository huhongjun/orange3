import pandas as pd
import numpy as np
import Orange

#### For those who are familiar with pandas
#### Correspondence:
####    value <-> Orange.data.Value
####        NaN <-> ["?", "~", "."] # Don't know, Don't care, Other
####    dtype <-> Orange.feature.Descriptor
####        category, int <-> Orange.feature.Discrete # category: > pandas 0.15
####        int, float <-> Orange.feature.Continuous # Continuous = core.FloatVariable
####                                                 # refer to feature/__init__.py
####        str <-> Orange.feature.String
####        object <-> Orange.feature.Python
####    DataFrame.dtypes <-> Orange.data.Domain
####    DataFrame.DataFrame <-> Orange.data.Table = Orange.orange.ExampleTable 
####                              # You will need this if you are reading sources

def series2descriptor(d, discrete=False):
    if d.dtype is np.dtype("float"):
        return Orange.feature.Continuous(str(d.name))
    elif d.dtype is np.dtype("int"):
        return Orange.feature.Continuous(str(d.name), number_of_decimals=0)
    else:
        t = d.unique()
        if discrete or len(t) < len(d) / 2:
            t.sort()
            return Orange.feature.Discrete(str(d.name), values=list(t.astype("str")))
        else:
            return Orange.feature.String(str(d.name))


def df2domain(df):
    featurelist = [series2descriptor(df.icol(col)) for col in xrange(len(df.columns))]
    return Orange.data.Domain(featurelist)


def df2table(df):
    # It seems they are using native python object/lists internally for Orange.data types (?)
    # And I didn't find a constructor suitable for pandas.DataFrame since it may carry
    # multiple dtypes
    #  --> the best approximate is Orange.data.Table.__init__(domain, numpy.ndarray),
    #  --> but the dtype of numpy array can only be "int" and "float"
    #  -->  * refer to src/orange/lib_kernel.cpp 3059:
    #  -->  *    if (((*vi)->varType != TValue::INTVAR) && ((*vi)->varType != TValue::FLOATVAR))
    #  --> Documents never mentioned >_<
    # So we use numpy constructor for those int/float columns, python list constructor for other

    tdomain = df2domain(df)
    ttables = [series2table(df.icol(i), tdomain[i]) for i in xrange(len(df.columns))]
    return Orange.data.Table(ttables)

    # For performance concerns, here are my results
    # dtndarray = np.random.rand(100000, 100)
    # dtlist = list(dtndarray)
    # tdomain = Orange.data.Domain([Orange.feature.Continuous("var" + str(i)) for i in xrange(100)])
    # tinsts = [Orange.data.Instance(tdomain, list(dtlist[i]) )for i in xrange(len(dtlist))] 
    # t = Orange.data.Table(tdomain, tinsts)
    #
    # timeit list(dtndarray)  # 45.6ms
    # timeit [Orange.data.Instance(tdomain, list(dtlist[i])) for i in xrange(len(dtlist))] # 3.28s
    # timeit Orange.data.Table(tdomain, tinsts) # 280ms

    # timeit Orange.data.Table(tdomain, dtndarray) # 380ms
    #
    # As illustrated above, utilizing constructor with ndarray can greatly improve performance
    # So one may conceive better converter based on these results


def series2table(series, variable):
    if series.dtype is np.dtype("int") or series.dtype is np.dtype("float"):
        # Use numpy
        # Table._init__(Domain, numpy.ndarray)
        return Orange.data.Table(Orange.data.Domain(variable), series.values[:, np.newaxis])
    else:
        # Build instance list
        # Table.__init__(Domain, list_of_instances)
        tdomain = Orange.data.Domain(variable)
        tinsts = [Orange.data.Instance(tdomain, [i]) for i in series]
        return Orange.data.Table(tdomain, tinsts)
        # 5x performance


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