#!/usr/bin/python
import os, io
import shutil
import copy
import lxml.etree as ET
from build_func import cleanXML
from build_func import toTXT

#namespace
tei_ns = {"tei" : "http://www.tei-c.org/ns/1.0"}

#prepare folder for new data
	#if directory exists, delete and create new ones
if os.path.exists("2_TEI") and os.path.isdir("2_TEI"):
    shutil.rmtree("2_TEI")
os.mkdir("2_TEI")
	#if directory exists, delete and create new ones
if os.path.exists("3_TXT") and os.path.isdir("3_TXT"):
    shutil.rmtree("3_TXT")
os.mkdir("3_TXT")

#Inspecting directory
for subdir in os.listdir("0_source"):
	#create sub-directory to paste new files afeter processing
	os.mkdir(os.path.join("2_TEI",subdir))
	print("""

		PRODUCING intermediary XML

	""")
	#print name of processed subdirectory to control the process along the way
	print('---', os.path.basename(subdir))
	directory=os.path.basename(subdir)
	#for each file in sub-directory
	for file in os.listdir(os.path.join("0_source",subdir)):
		#only xml files
		if file.endswith(".xml"):
			#print name of xml file to control the process along the way
			print('------', os.path.basename(file))
			#get body 0_source
			with open(os.path.join("0_source",subdir,file)) as f:
				xml = ET.parse(f)
				body = xml.xpath("//tei:TEI/tei:text | //text", namespaces = tei_ns)[0]
			#Erase/rename nodes
			body=cleanXML(body,directory)
			#get header in 1_header
			fileDalembert=os.path.splitext(file)[0]+"_dAlembert.xml"
			with open(os.path.join("1_header",subdir,fileDalembert)) as f:
				xml = ET.parse(f)
				header = xml.xpath("//tei:TEI", namespaces = tei_ns)[0]
				reg= xml.xpath("//tei:term[@type='reg']/@subtype", namespaces = tei_ns)[0]
				form= xml.xpath("//tei:term[@type='form']/@subtype", namespaces = tei_ns)[0]
				genre= xml.xpath("//tei:term[@type='genre']/@subtype", namespaces = tei_ns)[0]
				subgenre= xml.xpath("//tei:term[@type='subgenre']/@subtype", namespaces = tei_ns)[0]
			#find the tei:text in the header
			passage_to_erase = header.xpath("//tei:TEI/tei:text", namespaces = tei_ns)[0]
			# We remove the tei:text in the tei:header
			passage_to_erase.clear()
			#We replace the tei:text
			passage_to_replace = header.xpath("//tei:TEI/tei:text", namespaces = tei_ns)[0]
			#passage_to_replace.append(body)
			header.replace(passage_to_replace,body)
			#We save the result
			headerTree = ET.ElementTree(header)
			headerTree.write(os.path.join("2_TEI",subdir,file), pretty_print=True, xml_declaration=True, encoding="utf-8")
			print("Regularised? ",reg)
			print("Form: ",form)
			print("Genre: ",genre)
			print("Subgenre: ",subgenre)

	print("""

		PRODUCING TXT

	""")

	#for each file in sub-directory
	for file in os.listdir(os.path.join("2_TEI",subdir)):
		#only xml files
		if file.endswith(".xml"):
			#print name of xml file to control the process along the way
			print('------', os.path.basename(file))
			#get body 0_source
			with open(os.path.join("2_TEI",subdir,file)) as f:
				xml = ET.parse(f)
				text = xml.xpath("//tei:text", namespaces = tei_ns)[0]

			#Create txt
			text = toTXT(text)

			#We save the result
			fileTxt=os.path.splitext(file)[0]+"_dAlembert.txt"
			with io.open(os.path.join("3_TXT",fileTxt), "w", encoding="utf-8") as file:
				file.write(text)
				file.close()
