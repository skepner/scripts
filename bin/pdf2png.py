#! /usr/bin/env python

# For API notes see /Developer/Examples/Quartz/Python/API-SUMMARY

from CoreGraphics import *
import sys, os

if len (sys.argv) != 5:
    print "usage: %s <PDF file> <page-no-starting-with-1> <PNG file> <target-biggest-side-in-pixels>" % sys.argv[0]
    sys.exit(1)

(pdf_file, page_no, png_file, side) = sys.argv[1:]
page_no = int(page_no)
side = int(side)

pdf = CGPDFDocumentCreateWithProvider(CGDataProviderCreateWithFilename(pdf_file))
page = pdf.getPage(page_no)
media_box = page.getBoxRect(kCGPDFMediaBox)
aspect_ratio = media_box.size.width / media_box.size.height
if aspect_ratio < 1.0:
    target_width = int(side * aspect_ratio)
    target_height = int(side)
else:
    target_width = int(side)
    target_height = int(side / aspect_ratio)

cs = CGColorSpaceCreateWithName(kCGColorSpaceUserRGB)

ctx = CGBitmapContextCreateWithColor(target_width, target_height, cs, (0, 0, 0, 0, 1))
ctx.setInterpolationQuality(kCGInterpolationHigh)
ctx.drawPDFDocument(CGRectMake(0, 0, target_width, target_height), pdf, page_no)
ctx.writeToFile(png_file, kCGImageFormatPNG)
    
