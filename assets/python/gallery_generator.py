import re
import yaml

input_file = '/home/tzeny/Other/Projects/Websites/static_blog/_posts/2020-01-01-2019-year-in-review.md'

if __name__ == '__main__':
    with open(input_file, 'r') as file:
        lines =  file.readlines()

    regex = r'.*?<a href="(.*?)" title="(.*?)".*img src="(.*?)".*?\/a>.*?'

    pictures = []

    for line in lines:
        img_src_regex_match = re.match(regex, line)
        if img_src_regex_match:
            original = img_src_regex_match.group(1).replace('https://tzeny.com/wp-content/uploads/','assets/img/posts/')
            title = img_src_regex_match.group(2)
            thubmnail = img_src_regex_match.group(3).replace('https://tzeny.com/wp-content/uploads/','assets/img/posts/')

            pictures.append({
                'filename': original.split('/')[-1].split('.')[0],
                'original': original,
                'sizes': [original],
                'thumbnail': thubmnail,
                'title': title
            })

            # print(img_src_regex_match.groups())
            # break

    print(yaml.dump(pictures))



