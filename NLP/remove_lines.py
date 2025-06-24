word = "ezylicensing_spacy_text_PHH-01"
with open('/home/caratred/Documents/ram/Downloads/pos_checks_images/pos_checks_images/file_parsing.txt') as reader, open('/home/caratred/Documents/ram/Downloads/pos_checks_images/pos_checks_images/file_parsing.txt', 'r+') as writer:
  for line in reader:
    if line.strip():
      writer.write(line)
  writer.truncate()