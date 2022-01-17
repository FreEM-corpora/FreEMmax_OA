<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="3.0"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0">

    <xsl:output method="text" encoding="UTF-8"/>

    <xsl:variable name="xmlDocuments" select="collection('../1_header/?select=?*.xml;recurse=yes')"/>

    <xsl:template match="/">
        <xsl:text>Title</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Author</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Date</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Availability</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Genre</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Subgenre</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Form</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Regularisation</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>Nb of tokens (c.)</xsl:text>
        <xsl:text>&#09;</xsl:text>
        <xsl:text>File</xsl:text>
        <xsl:text>&#10;</xsl:text>
        <xsl:for-each select="$xmlDocuments">
            <xsl:value-of select="//titleStmt/title"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="//titleStmt/author"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="//sourceDesc/bibl/date/@when"/><xsl:value-of select="//sourceDesc/bibl/date/@from"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="//availability/@n"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="//textClass/keywords/term[@type='genre']/@subtype"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="//textClass/keywords/term[@type='subgenre']/@subtype"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="//textClass/keywords/term[@type='form']/@subtype"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="//textClass/keywords/term[@type='reg']/@subtype"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:variable name="content" select="//TEI" />
            <xsl:value-of select="count(tokenize($content, '\s+'))"/>
            <xsl:text>&#09;</xsl:text>
            <xsl:value-of select="base-uri()"/>
            <xsl:text>&#10;</xsl:text>
        </xsl:for-each>

    </xsl:template>

</xsl:stylesheet>
