
import os
import json
import sys
import csv
import zipfile

sys.path.insert(0, "./source/python/client")
from martiLQ import *

os.environ["MARTILQ_LOGPATH"] = "./test/python/results/logs"
        
print("Python sample/test case")

mlq = martiLQ()
mlq.LoadConfig(ConfigPath=None)
oMarti = mlq.NewMartiDefinition()
mlq.NewMartiChildItem(SourceFolder= "./docs/*", UrlPath="./docs" , ExcludeHash=False, ExtendAttributes=True)

oMarti["description"] = "Sample execution #1"

saveFile = "./test/python/results/martiLQ_docs_test_DocsPlain1.json"
mlq.Save(saveFile)
print("Saved martiLQ document: " + saveFile)

saveFile = "./test/python/results/martiLQ_docs_test_DocsPlain2.json"
oMarti["description"] = "Sample execution #2"
jsonFile = open(saveFile, "w")
jsonFile.write(json.dumps(oMarti, indent=5))
jsonFile.close()
print("Saved martiLQ document: " + saveFile)

saveFile = "./test/python/results/martiLQ_docs_test_DocsPlain1.json"
print("Load martiLQ document: "+saveFile)
mlq.Load(saveFile)
oMarti = mlq.Get()
print("Definition description is: {}".format(oMarti["description"]))

mlq.Close()

configPath = "./docs/source/samples/conf/GEN005.ini"
sourcePath = "./docs/source/*"
saveFile = "./test/python/results/martiLQ_docs_test_proc.json"
Make(ConfigPath=configPath, SourcePath=sourcePath, Filter="", Recursive=True, UrlPrefix="https://localhost/", DefinitionPath=saveFile)
print("Saved martiLQ document: " + saveFile)

sourcePath = "./test/python/results/data/*"
saveFile = "./test/python/results/martiLQ_docs_test_bsb.json"
Make(ConfigPath=configPath, SourcePath=sourcePath, Filter="BSBDirectory*", Recursive=True, UrlPrefix="http://apnedata.merebox.com.s3.ap-southeast-2.amazonaws.com/au/bsb/", DefinitionPath=saveFile)
print("Saved martiLQ document: " + saveFile)


print("Completed Python sample/test cases")