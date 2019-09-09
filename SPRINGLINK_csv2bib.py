import csv
import urllib.request

bib_files = []
with open('SpringLink_SearchResults.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        doi = row[5]
        line_count += 1

        if line_count > 1:
            filename = '{}.bib'.format(line_count)
            bib_files.append(filename)
            with open(filename, 'w') as f:
                url = "https://citation-needed.springer.com/v2/references/{}?format=bibtex&flavour=citation".format(doi)
                print(url)
                urllib.request.urlretrieve(url, filename)


print('TOTAL: ', line_count)



with open('springer.bib', 'w') as outfile:
    for fname in bib_files:
        with open(fname) as infile:
            outfile.write(infile.read())
