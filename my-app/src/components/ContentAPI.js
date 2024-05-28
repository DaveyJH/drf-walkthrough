import React, { Component } from 'react';
import css from "./css/Content.module.css";
import PostItemAPI from './PostItemAPI';
import Loader from './Loader';
import axios  from "axios";

export class Content extends Component {
  constructor(props) {
    super(props)
  
    this.state = {
      isLoaded: false,
      posts: [],
      savedPosts: [],
      error: null,
    }
  }

  componentDidMount() {
    this.fetchImages();
  }

  fetchImages = async () => {
    axios.get(
      `https://pixabay.com/api/?key=${
      process.env.REACT_APP_PIXABAY_API_KEY
      }&per_page=100`
    )
      .then(response => response.data.hits)
      .then(fetchedPosts => this.setState(
        prevState => ({ savedPosts: fetchedPosts })))
      .then(this.setState(prevState => ({ isLoaded: true})))
      .catch(e => this.setState(prevState => ({ error: e.message })))
  }

  handleOnChange = e => {
    const searchCriteria = e.target.value.toLowerCase();
    const filteredPosts = this.state.savedPosts.filter(
      post => post.tags.toLowerCase().includes(searchCriteria));
    this.setState(({ posts: filteredPosts }));
  }

  render() {
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
              onChange={ this.handleOnChange }/>
            <h4>posts found: { this.state.posts.length }</h4>
          </form>
        </div>
        { 
          this.state.error
            ? <p>{ this.state.error }</p>
            : <div className={ css.SearchResults }>
                {
                  this.state.isLoaded
                    ? document.getElementById("id-search-input").value.length
                      ? this.state.posts.map(post => (
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
}

export default Content