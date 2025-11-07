spark-submit --master yarn --deploy-mode cluster \
--py-files sbdl_lib.zip \
--files conf/sdbl.conf, conf/spark.conf, log4j.properties \
sbdl_main.py qa 2025-11-05