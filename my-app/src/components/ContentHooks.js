import React, { useState, useEffect } from 'react'
import css from "./css/Content.module.css";
import { savedPosts } from "../posts.json";
import PostItem from './PostItem';
import Loader from './Loader';

const ContentHooks = () => {
  const [isLoaded, setIsLoaded] = useState(false);
  const [fetchedPosts, setFetchedPosts] = useState([]);

  useEffect(() => {
    setTimeout(() => {
      setIsLoaded(true);
      setFetchedPosts(savedPosts);
    }, 2000)
  }, []);

  const handleChange = e => {
    const searchCriteria = e.target.value.toLowerCase();
    const filteredPosts = savedPosts.filter(
      post => post.title.toLowerCase().includes(searchCriteria));
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
        <div className={ css.SearchResults }>
          {
            isLoaded
              ? fetchedPosts.map(post => (
                  <PostItem post={ post } key={ post.title }/>
                ))
              : <Loader />
          }
        </div>
      </div>
  )
}

export default ContentHooks