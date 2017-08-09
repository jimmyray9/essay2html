import html, string, os, sys

with open('C:\Users\Administrator\Desktop\search\phrases') as wdlst_raw:
	words = wdlst_raw.read().split('\n')
with open('C:\Users\Administrator\Desktop\search\\transitions') as t_raw:
	transitionals = t_raw.read().split('\n')
with open('C:\Users\Administrator\Desktop\search\hedging') as h_raw:
	hedging = h_raw.read().split('\n')
with open('C:\Users\Administrator\Desktop\search\\reporting_verbs') as r_raw:
	reportings = r_raw.read().split('\n')
with open('C:\Users\Administrator\Desktop\search\cause_effect') as c_raw:
	causes = c_raw.read().split('\n')



#open the current working directory
path = os.getcwd()
dirs = os.listdir(path)

#Print out all the text files without extension and add to list called "text_files"
text_files = []
for file in dirs:
	filesplit = os.path.splitext(file)
	if filesplit[1] == '.txt':
		text_files.append(file)

#opens each file from text_list and reads it to p_read
for text in text_files:
	h = html.HTML()
	file_ = open(text, 'r') 
	p_read = file_.readlines()
	file_.close()
	#opens a html to write to	
	new_f = open(filesplit + '.html', 'w+')
	#each line from the document gets sent to the html page as a <p>
	for line in p_read:
		#checks each line for words from the list "words"
		for word in words:
			line = string.replace(line, word , "<span style='background-color:#A175AA'>{}</span>".format(word))
			#checks each line for the words from the list "transitional"
		for transitional in transitionals:
			line = string.replace(line, transitional , "<span style='background-color:#B3B0FC'>{}</span>".format(transitional))
		for hedge in hedging:
			line = string.replace(line, hedge , "<span style='background-color:#348AA7'>{}</span>".format(hedge))
		for cause in causes:
			line = string.replace(line, cause , "<span style='background-color:#5DD39E'>{}</span>".format(cause))
		for report in reportings:
			line = string.replace(line, report , "<span style='background-color:#BCE784'>{}</span>".format(report))

	h.p(line, escape=False)
	#writes to the new html file then closes it
	new_f.write(str(h))
	new_f.close()

