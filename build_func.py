#!/usr/bin/python
import lxml.etree as ET
import re

tei_ns = {
					"tei" : "http://www.tei-c.org/ns/1.0",
					"xml": "http://www.w3.org/XML/1998/namespace",
					"re": "http://exslt.org/regular-expressions"
					}

#Warning:
#Deal with reg/orig depending on term/@reg.
#Deal with front and back too.
#Deal with foreign languaages in foreign or @xml:lang

def cleanXML(doc,directory):
	#Transform to string to perform basic replacements
	docStr = ET.tostring(doc, encoding="unicode")

	#Forget about namespace
	docStr = docStr.replace(' xmlns="http://www.tei-c.org/ns/1.0"', '')

	#add carriage return
	docStr = docStr.replace(r'<\/p>\s?<p>', '<\/p>\n<p>')

	#Avoid agglutination
	docStr = docStr.replace('><', '> <')

	#Transform back to lxml tree object
	doc = ET.fromstring(docStr, parser=ET.XMLParser(huge_tree=True))

	#Delete tags+content
	#for some repo, the front and the back has to be deleted
	if directory=="dramacode":
		print("we delete the back and the front")
		ET.strip_elements(doc, 'front', with_tail=False)
		ET.strip_elements(doc, 'back', with_tail=False)
	else:
		print("we keep the back and the front")
	ET.strip_elements(doc, 'milestone', with_tail=False)
	ET.strip_elements(doc, 'reg', with_tail=False)
	ET.strip_elements(doc, 'gap', with_tail=False)
	ET.strip_elements(doc, 'del', with_tail=False)
	ET.strip_elements(doc, 'bib', with_tail=False)
	ET.strip_elements(doc, 'sic', with_tail=False)
	ET.strip_elements(doc, 'fw', with_tail=False)
	ET.strip_elements(doc, 'note', with_tail=False)
	ET.strip_elements(doc, 'castList', with_tail=False)
	ET.strip_elements(doc, 'docTitle', with_tail=False)
	ET.strip_elements(doc, 'ref', with_tail=False)
	ET.strip_elements(doc, 'figure', with_tail=False)
	ET.strip_elements(doc, 'space', with_tail=False)
	ET.strip_elements(doc, 'bibl', with_tail=False)
	ET.strip_elements(doc, 'idno[@role=\'author\']', with_tail=False)
	ET.strip_elements(doc, 'idno[parent::item]', with_tail=False)
	ET.strip_elements(doc, 'term[@type=\'gender\']', with_tail=False)
	#Strange elements of Theatre classique
	ET.strip_elements(doc, 'performance', with_tail=False)
	ET.strip_elements(doc, 'premiere', with_tail=False)
	ET.strip_elements(doc, 'bottom', with_tail=False)
	ET.strip_elements(doc, 'rdg', with_tail=False)
	ET.strip_elements(doc, 'ptr', with_tail=False)
	ET.strip_elements(doc, 'formula', with_tail=False)
	ET.strip_elements(doc, 'graphic', with_tail=False)

	#Delete tags
	ET.strip_tags(doc, 'fs',)
	ET.strip_tags(doc, 'pc',)
	ET.strip_tags(doc, 'index',)
	ET.strip_tags(doc, 'term',)
	ET.strip_tags(doc, 'q',)
	ET.strip_tags(doc, 'publisher',)
	ET.strip_tags(doc, 'pubPlace',)
	ET.strip_tags(doc, 'surplus',)
	ET.strip_tags(doc, 'unclear',)
	ET.strip_tags(doc, 'foreign',)
	ET.strip_tags(doc, 'sic')
	ET.strip_tags(doc, 'corr')
	ET.strip_tags(doc, 'choice')
	ET.strip_tags(doc, 'orig')
	ET.strip_tags(doc, 'g')
	ET.strip_tags(doc, 'subst')
	ET.strip_tags(doc, 'rs')
	ET.strip_tags(doc, 'app')
	ET.strip_tags(doc, 'lem')
	ET.strip_tags(doc, 'quote')
	ET.strip_tags(doc, 'cit')
	ET.strip_tags(doc, 'supplied')
	ET.strip_tags(doc, 'seg')
	ET.strip_tags(doc, 'add')
	ET.strip_tags(doc, 'c')
	ET.strip_tags(doc, 'cb')
	ET.strip_tags(doc, 'expan')
	ET.strip_tags(doc, 'abbr')
	ET.strip_tags(doc, 'cb')
	ET.strip_tags(doc, 'genName')
	ET.strip_tags(doc, 'w')
	ET.strip_tags(doc, 's')
	ET.strip_tags(doc, 'front')
	ET.strip_tags(doc, 'hi')

	#Rename elements
	for div0 in doc.xpath("//div0"):
		div0.tag = 'div'
	for div1 in doc.xpath("//div1"):
		div1.tag = 'div'
	for div2 in doc.xpath("//div2"):
		div2.tag = 'div'
	for div3 in doc.xpath("//div3"):
		div3.tag = 'div'
	for div4 in doc.xpath("//div4"):
		div4.tag = 'div'
	for div5 in doc.xpath("//div5"):
		div5.tag = 'div'
	for ab in doc.xpath("//ab"):
		ab.tag = 'p'
	for imprimatur in doc.xpath("//imprimatur"):
		imprimatur.tag = 'p'
	for docImprint in doc.xpath("//docImprint"):
		docImprint.tag = 'p'
	for docAuthor in doc.xpath("//docAuthor"):
		docAuthor.tag = 'p'
	for titlePage in doc.xpath("//titlePage"):
		titlePage.tag = 'div'
	for docDate in doc.xpath("//docDate"):
		docDate.tag = 'p'
	for placeName in doc.xpath("//placeName"):
		placeName.tag = 'name'
	for persName in doc.xpath("//persName"):
		persName.tag = 'name'
	for geogName in doc.xpath("//geogName"):
		geogName.tag = 'name'
	for geogFeat in doc.xpath("//geogFeat"):
		geogFeat.tag = 'name'
	for orgName in doc.xpath("//orgName"):
		orgName.tag = 'name'
	for sett in doc.xpath("//set"):
		sett.tag = 'p'
	#Invented elements of theatre classique
	for adresse in doc.xpath("//adresse"):
		adresse.tag = 'p'
	for signature in doc.xpath("//signature"):
		signature.tag = 'p'
	for privilege in doc.xpath("//privilege"):
		privilege.tag = 'p'
	for enregistrement in doc.xpath("//enregistrement"):
		enregistrement.tag = 'p'
	for approbation in doc.xpath("//approbation"):
		approbation.tag = 'p'
	for printer in doc.xpath("//printer"):
		printer.tag = 'p'
	for acheveImprime in doc.xpath("//acheveImprime"):
		acheveImprime.tag = 'p'
	for titlePart in doc.xpath("//titlePart"):
		titlePart.tag = 'p'
	for editor in doc.xpath("//editor"):
		editor.tag = 'p'

	#Delete attributes
	ET.strip_attributes(doc, 'ana')
	ET.strip_attributes(doc, 'ed')
	ET.strip_attributes(doc, 'part')
	ET.strip_attributes(doc, 'rend')
	ET.strip_attributes(doc, 'rendition')
	ET.strip_attributes(doc, 'n')
	ET.strip_attributes(doc, 'xml:lang')
	ET.strip_attributes(doc, 'key')
	ET.strip_attributes(doc, 'facs')
	ET.strip_attributes(doc, 'id')
	ET.strip_attributes(doc, 'rest')
	ET.strip_attributes(doc, 'copyOf')
	ET.strip_attributes(doc, 'met')
	for xmlLang in doc.xpath("//*[@xml:lang]"):
		xmlLang.attrib.clear()
	#Strange attribtues from theatre classique
	ET.strip_attributes(doc, 'bio')
	ET.strip_attributes(doc, 'location')
	ET.strip_attributes(doc, 'country')
	ET.strip_attributes(doc, 'gps')
	ET.strip_attributes(doc, 'value')
	ET.strip_attributes(doc, 'stage')
	ET.strip_attributes(doc, 'stage')
	ET.strip_attributes(doc, 'syll')
	ET.strip_attributes(doc, 'periode')
	for stage in doc.xpath("//*[@type='v']"):
		stage.attrib.clear()
	#APWCF
	ET.strip_attributes(doc, 'rec1')
	ET.strip_attributes(doc, 'rec2')
	ET.strip_attributes(doc, 'rec3')
	ET.strip_attributes(doc, 'dat')
	ET.strip_attributes(doc, 'loc')
	ET.strip_attributes(doc, 'aut1')
	ET.strip_attributes(doc, 'aut2')
	ET.strip_attributes(doc, 'aut3')
	ET.strip_attributes(doc, 'sub')
	ET.strip_attributes(doc, 'vol')
	ET.strip_attributes(doc, 'nr')
	ET.strip_attributes(doc, 'when')

	return doc


def toTXT(doc):
	#Pasting split words accross lines with <lb type="hyphen"/>
	docStr = ET.tostring(doc, encoding="unicode")
	docStr = re.sub(r'-[\s\r\n]*<lb rend="hyphen"/>\s*', '', docStr)
	docStr = re.sub(r'\n+', '\n', docStr)
	docStr = docStr.replace(' l\' ' ,'l\'')
	docStr = docStr.replace(' n\' ' ,'n\'')
	docStr = docStr.replace(' m\' ' ,'m\'')
	docStr = docStr.replace(' c\' ' ,'c\'')
	#docStr = re.sub('&amp;', '&', docStr)
	docStr = docStr.replace(' xmlns="http://www.tei-c.org/ns/1.0"', '')
	doc = ET.fromstring(docStr, parser=ET.XMLParser(huge_tree=True))

	#Avoid agglutination
	ET.strip_tags(doc, 'body')
	ET.strip_tags(doc, 'p')
	ET.strip_tags(doc, 'l')
	ET.strip_tags(doc, 'head')
	ET.strip_tags(doc, 'div')
	ET.strip_tags(doc, 'name')
	ET.strip_tags(doc, 'lb')
	ET.strip_tags(doc, 'text')
	ET.strip_tags(doc, 'pb')
	ET.strip_tags(doc, 'stage')
	ET.strip_tags(doc, 'sp')
	ET.strip_tags(doc, 'speaker')
	ET.strip_tags(doc, 'bibl')

	for div1 in doc.xpath("//div1"):
		div1.tag = 'div'

	#Pasting split words accross lines with <lb type="hyphen"/>
	doc = ET.tostring(doc, encoding="unicode")
	#get rid of entities
	doc = doc.replace('&amp;', '&')
	#get rid of root element
	doc = doc.replace("<text>","")
	doc = doc.replace("</text>","")

	return doc
