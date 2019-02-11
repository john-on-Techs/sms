document.write('<link rel="stylesheet" href="https://github.githubassets.com/assets/gist-embed-b3b573358bfc66d89e1e95dbf8319c09.css">')
document.write('<div id=\"gist85474599\" class=\"gist\">\n    <div class=\"gist-file\">\n      <div class=\"gist-data\">\n        <div class=\"js-gist-file-update-container js-task-list-container file-box\">\n  <div id=\"file-models-py\" class=\"file\">\n    \n\n  <div itemprop=\"text\" class=\"blob-wrapper data type-python \">\n      \n<table class=\"highlight tab-size js-file-line-container\" data-tab-size=\"8\">\n      <tr>\n        <td id=\"file-models-py-L1\" class=\"blob-num js-line-number\" data-line-number=\"1\"><\/td>\n        <td id=\"file-models-py-LC1\" class=\"blob-code blob-code-inner js-file-line\"><span class=\"pl-k\">class<\/span> <span class=\"pl-en\">ReportRequest<\/span>(<span class=\"pl-e\">models<\/span>.<span class=\"pl-e\">Model<\/span>):<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L2\" class=\"blob-num js-line-number\" data-line-number=\"2\"><\/td>\n        <td id=\"file-models-py-LC2\" class=\"blob-code blob-code-inner js-file-line\">    host <span class=\"pl-k\">=<\/span> models.CharField(<span class=\"pl-v\">max_length<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">1000<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L3\" class=\"blob-num js-line-number\" data-line-number=\"3\"><\/td>\n        <td id=\"file-models-py-LC3\" class=\"blob-code blob-code-inner js-file-line\">    path <span class=\"pl-k\">=<\/span> models.CharField(<span class=\"pl-v\">max_length<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">1000<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L4\" class=\"blob-num js-line-number\" data-line-number=\"4\"><\/td>\n        <td id=\"file-models-py-LC4\" class=\"blob-code blob-code-inner js-file-line\">    method <span class=\"pl-k\">=<\/span> models.CharField(<span class=\"pl-v\">max_length<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">50<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L5\" class=\"blob-num js-line-number\" data-line-number=\"5\"><\/td>\n        <td id=\"file-models-py-LC5\" class=\"blob-code blob-code-inner js-file-line\">    uri <span class=\"pl-k\">=<\/span> models.CharField(<span class=\"pl-v\">max_length<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">2000<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L6\" class=\"blob-num js-line-number\" data-line-number=\"6\"><\/td>\n        <td id=\"file-models-py-LC6\" class=\"blob-code blob-code-inner js-file-line\">    status_code <span class=\"pl-k\">=<\/span> models.IntegerField()<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L7\" class=\"blob-num js-line-number\" data-line-number=\"7\"><\/td>\n        <td id=\"file-models-py-LC7\" class=\"blob-code blob-code-inner js-file-line\">    remote_addr <span class=\"pl-k\">=<\/span> models.IPAddressField()<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L8\" class=\"blob-num js-line-number\" data-line-number=\"8\"><\/td>\n        <td id=\"file-models-py-LC8\" class=\"blob-code blob-code-inner js-file-line\">    remote_addr_fwd <span class=\"pl-k\">=<\/span> models.IPAddressField(<span class=\"pl-v\">blank<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">True<\/span>, <span class=\"pl-v\">null<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">True<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L9\" class=\"blob-num js-line-number\" data-line-number=\"9\"><\/td>\n        <td id=\"file-models-py-LC9\" class=\"blob-code blob-code-inner js-file-line\">    request_meta <span class=\"pl-k\">=<\/span> models.TextField()<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L10\" class=\"blob-num js-line-number\" data-line-number=\"10\"><\/td>\n        <td id=\"file-models-py-LC10\" class=\"blob-code blob-code-inner js-file-line\">    query <span class=\"pl-k\">=<\/span> models.TextField()<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L11\" class=\"blob-num js-line-number\" data-line-number=\"11\"><\/td>\n        <td id=\"file-models-py-LC11\" class=\"blob-code blob-code-inner js-file-line\">    user <span class=\"pl-k\">=<\/span> models.ForeignKey(User, <span class=\"pl-v\">on_delete<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">None<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L12\" class=\"blob-num js-line-number\" data-line-number=\"12\"><\/td>\n        <td id=\"file-models-py-LC12\" class=\"blob-code blob-code-inner js-file-line\">    types <span class=\"pl-k\">=<\/span> (<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L13\" class=\"blob-num js-line-number\" data-line-number=\"13\"><\/td>\n        <td id=\"file-models-py-LC13\" class=\"blob-code blob-code-inner js-file-line\">        (<span class=\"pl-c1\">0<\/span>, <span class=\"pl-s\"><span class=\"pl-pds\">&quot;<\/span>Email<span class=\"pl-pds\">&quot;<\/span><\/span>),<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L14\" class=\"blob-num js-line-number\" data-line-number=\"14\"><\/td>\n        <td id=\"file-models-py-LC14\" class=\"blob-code blob-code-inner js-file-line\">        (<span class=\"pl-c1\">1<\/span>, <span class=\"pl-s\"><span class=\"pl-pds\">&quot;<\/span>Browser<span class=\"pl-pds\">&quot;<\/span><\/span>),<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L15\" class=\"blob-num js-line-number\" data-line-number=\"15\"><\/td>\n        <td id=\"file-models-py-LC15\" class=\"blob-code blob-code-inner js-file-line\">    )<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L16\" class=\"blob-num js-line-number\" data-line-number=\"16\"><\/td>\n        <td id=\"file-models-py-LC16\" class=\"blob-code blob-code-inner js-file-line\">    request_type <span class=\"pl-k\">=<\/span> models.IntegerField(<span class=\"pl-v\">choices<\/span><span class=\"pl-k\">=<\/span>types)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L17\" class=\"blob-num js-line-number\" data-line-number=\"17\"><\/td>\n        <td id=\"file-models-py-LC17\" class=\"blob-code blob-code-inner js-file-line\">    success <span class=\"pl-k\">=<\/span> models.BooleanField(<span class=\"pl-v\">default<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">True<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L18\" class=\"blob-num js-line-number\" data-line-number=\"18\"><\/td>\n        <td id=\"file-models-py-LC18\" class=\"blob-code blob-code-inner js-file-line\">    created_at <span class=\"pl-k\">=<\/span> models.DateTimeField(<span class=\"pl-v\">auto_now_add<\/span><span class=\"pl-k\">=<\/span><span class=\"pl-c1\">True<\/span>)<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L19\" class=\"blob-num js-line-number\" data-line-number=\"19\"><\/td>\n        <td id=\"file-models-py-LC19\" class=\"blob-code blob-code-inner js-file-line\">\n<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L20\" class=\"blob-num js-line-number\" data-line-number=\"20\"><\/td>\n        <td id=\"file-models-py-LC20\" class=\"blob-code blob-code-inner js-file-line\">    <span class=\"pl-k\">class<\/span> <span class=\"pl-en\">Meta<\/span>:<\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L21\" class=\"blob-num js-line-number\" data-line-number=\"21\"><\/td>\n        <td id=\"file-models-py-LC21\" class=\"blob-code blob-code-inner js-file-line\">        db_table <span class=\"pl-k\">=<\/span> <span class=\"pl-s\"><span class=\"pl-pds\">&quot;<\/span>tutorial_pdf_requests<span class=\"pl-pds\">&quot;<\/span><\/span><\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L22\" class=\"blob-num js-line-number\" data-line-number=\"22\"><\/td>\n        <td id=\"file-models-py-LC22\" class=\"blob-code blob-code-inner js-file-line\">        verbose_name <span class=\"pl-k\">=<\/span> <span class=\"pl-s\"><span class=\"pl-pds\">&quot;<\/span>Report Request<span class=\"pl-pds\">&quot;<\/span><\/span><\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L23\" class=\"blob-num js-line-number\" data-line-number=\"23\"><\/td>\n        <td id=\"file-models-py-LC23\" class=\"blob-code blob-code-inner js-file-line\">        verbose_name_plural <span class=\"pl-k\">=<\/span> <span class=\"pl-s\"><span class=\"pl-pds\">&quot;<\/span>Report Requests<span class=\"pl-pds\">&quot;<\/span><\/span><\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L24\" class=\"blob-num js-line-number\" data-line-number=\"24\"><\/td>\n        <td id=\"file-models-py-LC24\" class=\"blob-code blob-code-inner js-file-line\">        <\/td>\n      <\/tr>\n      <tr>\n        <td id=\"file-models-py-L25\" class=\"blob-num js-line-number\" data-line-number=\"25\"><\/td>\n        <td id=\"file-models-py-LC25\" class=\"blob-code blob-code-inner js-file-line\">        <\/td>\n      <\/tr>\n<\/table>\n\n\n  <\/div>\n\n  <\/div>\n<\/div>\n\n      <\/div>\n      <div class=\"gist-meta\">\n        <a href=\"https://gist.github.com/bencleary/6f3e0b7bc22d57609e3c55c913ccfba6/raw/1f96e78845c0e7b49b92917b805da2a445e01910/models.py\" style=\"float:right\">view raw<\/a>\n        <a href=\"https://gist.github.com/bencleary/6f3e0b7bc22d57609e3c55c913ccfba6#file-models-py\">models.py<\/a>\n        hosted with &#10084; by <a href=\"https://github.com\">GitHub<\/a>\n      <\/div>\n    <\/div>\n<\/div>\n')
