import React, { Component } from 'react';
import css from "./css/Content.module.css";
import PostItem from './PostItem';
import { savedPosts } from "../posts.json";
import Loader from './Loader';

export class Content extends Component {
  constructor(props) {
    super(props)
  
    this.state = {
      isLoaded: false,
      posts: [],
    }
  }

  componentDidMount() {
    this.setState({ posts: savedPosts })
    setTimeout(() => {
      this.setState(prevState => ({
        isLoaded: !prevState.isLoaded
      }))
    }, 2000)
  }

  handleOnChange = e => {
    const searchCriteria = e.target.value.toLowerCase();
    const filteredPosts = savedPosts.filter(
      post => post.title.toLowerCase().includes(searchCriteria));
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
        <div className={ css.SearchResults }>
          {
            this.state.isLoaded
              ? this.state.posts.map(post => (
                <PostItem post={ post } key={ post.title }/>
              ))
              : <Loader />
          }
        </div>
      </div>
    )
  }
}

export default Content