#!/usr/bin/env python
import glob
import os
import yaml

tag_db_path = '_data/tag-format.yml'

with open(tag_db_path) as f:
    tag_db = yaml.load(f, Loader=yaml.FullLoader)

    # Gather all of the used tags in posting.
    posts = glob.glob('_posts/**/*md', recursive=True)
    current_used_tags = []
    for post in posts:
        f = open(post, 'r')
        crawl = False
        for line in f:
            if crawl:
                current_tags = line.strip().split()
                if current_tags[0] == 'tags:':
                    current_used_tags.extend(current_tags[1:])
                    crawl = False
                    break
            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break
        f.close()

    # Check if there is an unavailable tag.
    current_used_tags = set(current_used_tags)
    for tag in current_used_tags:
        if tag not in tag_db:
            raise Exception(f'{tag} does not exist in {tag_db_path}')

    # Remove unused tag markdown files for now.
    tag_dir = 'blog/tags/'
    if not os.path.exists(tag_dir):
        os.makedirs(tag_dir)

    old_tag_md_files = glob.glob(tag_dir + '*.md')
    for file_path in old_tag_md_files:
        tag = os.path.basename(file_path).split(".md")[0]
        if tag not in current_used_tags:
            os.remove(file_path)

    # Update tag markdown files that are used in blogging.
    for tag in current_used_tags:
        file_path = tag_dir + tag + '.md'
        with open(file_path, 'w') as f2:
            f2.write('---\nlayout: tagpage\ntitle: \"' + tag_db[tag] + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n')

print('Tags generated, count:', len(current_used_tags))
print(f'Used/Total = {len(current_used_tags)}/{len(tag_db)}')
