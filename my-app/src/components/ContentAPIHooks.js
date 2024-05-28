import React, { useState, useEffect } from 'react'
import css from "./css/Content.module.css";
import PostItemAPI from './PostItemAPI';
import PostItem from './PostItem';
import Loader from './Loader';

const ContentHooks = () => {
  const [isLoaded, setIsLoaded] = useState(false);
  const [fetchedPosts, setFetchedPosts] = useState([]);
  const [savedPosts, setSavedPosts] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchImages();
  }, []);

  const fetchImages = async () => {
    axios.get(
      `https://pixabay.com/api/?key=${
      process.env.REACT_APP_PIXABAY_API_KEY
      }&per_page=100`
    )
      .then(response => response.data.hits)
      .then(posts => setSavedPosts(posts))
      .then(setIsLoaded(true))
      .catch(e => setError(e.message))
    }

  const handleChange = e => {
    const searchCriteria = e.target.value.toLowerCase();
    const filteredPosts = savedPosts.filter(
      post => post.tags.toLowerCase().includes(searchCriteria));
    setFetchedPosts(filteredPosts);
  }

  return (
    <div className={ css.Content }>
        <div className={ css.TitleBar }>
          <h1>My Photos</h1>
          <form>
            <label htmlFor="id-search-input">Search:</label>
            <input
              type="search" 
              name="search-input" 
              id="id-search-input"
              onChange={ e => handleChange(e) }/>
            <h4>posts found: { isLoaded ? fetchedPosts.length : "loading posts..." }</h4>
          </form>
        </div>
        { 
          error
            ? <p>{ error }</p>
            : <div className={ css.SearchResults }>
                {
                  isLoaded
                    ? document.getElementById("id-search-input").value.length
                      ? posts.map(post => (
                        <PostItemAPI post={ post } key={ post.title }/>
                      ))
                      : <p>Please provide a search query.</p>
                    : <Loader />
                }
              </div>
        }
      </div>
  )
}

export default ContentHooks