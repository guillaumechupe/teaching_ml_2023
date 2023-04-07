#1.1_EncoderFeaturesNONNumériques_GuillaumeCHUPE

def encode_ordinal(data, cols):
    """
    Encodes the columns specified in cols using ordinal encoding.

    Parameters:
    data (DataFrame): The dataframe containing the columns to encode.
    cols (list): The list of column names to encode.

    Returns:
    DataFrame: The dataframe with encoded columns.
    """
    encoder = OrdinalEncoder()
    data[cols] = encoder.fit_transform(data[cols])
    return data


def encode_onehot(data, cols):
    """
    Encodes the columns specified in cols using one-hot encoding.

    Parameters:
    data (DataFrame): The dataframe containing the columns to encode.
    cols (list): The list of column names to encode.

    Returns:
    DataFrame: The dataframe with encoded columns.
    """
    encoder = OneHotEncoder()
    encoded_cols = encoder.fit_transform(data[cols])
    encoded_data = pd.DataFrame(encoded_cols.toarray(), columns=encoder.get_feature_names(cols))
    data = data.drop(columns=cols)
    data = pd.concat([data, encoded_data], axis=1)
    return data


def encode_hash(data, cols, n_components):
    """
    Encodes the columns specified in cols using hashing encoding.

    Parameters:
    data (DataFrame): The dataframe containing the columns to encode.
    cols (list): The list of column names to encode.
    n_components (int): The number of dimensions in the encoding.

    Returns:
    DataFrame: The dataframe with encoded columns.
    """
    encoder = HashingEncoder(n_components=n_components)
    encoded_cols = encoder.fit_transform(data[cols])
    encoded_data = pd.DataFrame(encoded_cols)
    data = data.drop(columns=cols)
    data = pd.concat([data, encoded_data], axis=1)
    return data


def encode_count(data, cols):
    """
    Encodes the columns specified in cols by counting the occurrences of values.

    Parameters:
    data (DataFrame): The dataframe containing the columns to encode.
    cols (list): The list of column names to encode.

    Returns:
    DataFrame: The dataframe with encoded columns.
    """
    encoder = CountEncoder()
    data[cols] = encoder.fit_transform(data[cols])
    return data