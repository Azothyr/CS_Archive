import pytest
from cluster_csv_handler import ClusterCSVHandler
from pyspark.sql import DataFrame, SparkSession


@pytest.fixture
def spark_session():
    return SparkSession.builder \
                .master("local[*]") \
                .config("spark.driver.host", "localhost") \
                .appName("Test") \
                .getOrCreate()


@pytest.fixture
def csv_handler(spark_session):
    return ClusterCSVHandler('dummy.csv', master='local[*]', app_name='Test', driver_host='localhost')


def test_cluster_handler_initialization(csv_handler):
    assert csv_handler.file_path == 'dummy.csv'


def test_cluster_handler_read_data_failure(csv_handler):
    with pytest.raises(RuntimeError) as e:
        csv_handler._read_data()
    assert 'Failed to read data' in str(e.value)


def test_cluster_handler_process_data(csv_handler, spark_session):
    data = spark_session.createDataFrame([('Alice', 1), ('Bob', 2)], ['name', 'age'])
    processed_data = csv_handler._process_data(data, ['name'])
    assert isinstance(processed_data, DataFrame)
    assert processed_data.columns == ['name']


def test_cluster_handler_get_data_failure(csv_handler):
    with pytest.raises(RuntimeError) as e:
        csv_handler.get_data(['name'])
    assert 'Failed to read data' in str(e.value)
