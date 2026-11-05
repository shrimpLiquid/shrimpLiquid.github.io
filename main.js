// 1. Setup the function that processes your post data when it arrives
window.handleTumblrData = function(data) {
  const container = document.getElementById('sidetext');
  
  if (!data || !data.posts || data.posts.length === 0) {
    container.innerText = "No posts found with this tag.";
    return;
  }

  // Grab the single most recent post returned from your blog
  const latestPost = data.posts[0]; 
  
  // Render the post body layout text into your HTML container
  container.innerHTML = latestPost['text-body'] || latestPost['body'] || latestPost['caption'] || "Empty post content.";
};

// 2. Build the script source URL using simple string pieces glued together
function fetchLatestTaggedPost(blogName, tagName) {
  const script = document.createElement('script');
  
  // Glue every individual part together explicitly to guarantee a correct layout path
  const part1 = "https://" + blogName;
  const part2 = "://";
  const part3 = encodeURIComponent(tagName);
  const part4 = "&num=1&callback=handleTumblrData";
  
  script.src = part1 + part2 + part3 + part4;
  
  document.body.appendChild(script);
}

// 3. Fire the request with your username and your tag
fetchLatestTaggedPost('shrimpliquid', 'wordslopoftheyear');
