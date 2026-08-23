import re

def solution(word, pages):
    n = len(pages)
    word = word.lower()

    urls = []
    basics = []
    links = []

    for page in pages:
        url = re.search(r'<meta property="og:url" content="(.*?)"', page).group(1)
        urls.append(url)

        words = re.findall(r'[a-zA-Z]+', page)
        basics.append(sum(w.lower() == word for w in words))

        links.append(re.findall(r'<a href="(.*?)">', page))

    url_to_idx = {url: i for i, url in enumerate(urls)}
    link_scores = [0.0] * n

    for i in range(n):
        if not links[i]:
            continue

        score = basics[i] / len(links[i])

        for url in links[i]:
            if url in url_to_idx:
                link_scores[url_to_idx[url]] += score

    scores = [basics[i] + link_scores[i] for i in range(n)]

    return max(range(n), key=lambda i: scores[i])