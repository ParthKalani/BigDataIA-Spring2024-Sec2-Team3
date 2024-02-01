from diagrams import Diagram, Cluster
from diagrams.onprem.analytics import Spark
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.database import PostgreSQL
from diagrams.aws.analytics import ManagedStreamingForKafka
from diagrams.onprem.queue import RabbitMQ
from diagrams.onprem.aggregator import Fluentd
from diagrams.saas.cdn import Akamai
from diagrams.aws.storage import S3
from diagrams.onprem.client import User
from diagrams.onprem import Node

with Diagram("Lambda Architecture for IntelliBuy Pipeline", show=True, direction="TB"):
    with Cluster("Product APIs", graph_attr={"fontsize": "10", "rankdir": "LR"}):
        api1 =  Node("Target API", image="target.png")
        api2 =  Node("BestBuy API", image="bestbuy.png")
        api3 =  Node("Amazon API", image="amazon.png")
        
    with Cluster("Lambda Architecture"):
        with Cluster("Batch Layer"):
            batch = [Airflow("Airflow Scheduler"),
                     Spark("Spark Processing")]
            api2 >> batch

        with Cluster("Speed Layer"):
            speed = ManagedStreamingForKafka("Kafka Stream Processing")
            api2 >> speed

        with Cluster("Serving Layer"):
            serving = PostgreSQL("PostgreSQL")
            batch >> serving
            speed >> serving