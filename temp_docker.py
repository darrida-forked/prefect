from typing import Tuple, Optional

"""
// splitReposSearchTerm breaks a search term into an index name and remote name
func splitReposSearchTerm(reposName string) (string, string) {
        nameParts := strings.SplitN(reposName, "/", 2)
        var indexName, remoteName string
        if len(nameParts) == 1 || (!strings.Contains(nameParts[0], ".") &&
                !strings.Contains(nameParts[0], ":") && nameParts[0] != "localhost") {
                // This is a Docker Index repos (ex: samalba/hipache or ubuntu)
                // 'docker.io'
                indexName = IndexName
                remoteName = reposName
        } else {
                indexName = nameParts[0]
                remoteName = nameParts[1]
        }
        return indexName, remoteName
}
"""

def parse_tag_image(name: str) -> Tuple[str, Optional[str]]:
    tag_name = None
    name_parts = name.split('/')
    if len(name_parts) == 1 and name_parts[0] != 'localhost':
        if ':' in name_parts[0]:
            image_name, tag_name = name_parts[0].split(':')    # i.e., simple_name:latest
        else:
            image_name = name_parts[0]                         # i.e., simple_name
    else:
        index_name = name_parts[0]             # i.e., gitlab.waubonsee.edu:5050
        image_path = '/'.join(name_parts[1:])  # i.e., folder/subfolder/repo:latest
        if ':' in image_path:
            image_path, tag_name = image_path.split(':')
        image_name = f"{index_name}/{image_path}"
    return image_name, tag_name


images = [
    'sample.image:2.1.1',
    'localhost/sample_image',
    'localhost/sample_image:2.1.1',
    'prefecthq/prefect',
    'prefecthq/prefect:2.1.1',
    'sample_image',
    'sample_image:2.1.1',
    'sample_image:latest',
    'sample_image:5050/repo/folder',
    'sample_image:5050/repo/folder:2.1.1',
    'sample_image:5050/repo/folder:latest'
]


for i in images:
    print(f"PASSED IN: {i}")
    result = parse_tag_image(i)
    print(f"    IMAGE: {result[0]} | TAG => {result[1]}")
    print()
