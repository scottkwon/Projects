import { GithubscorePage } from './app.po';

describe('githubscore App', () => {
  let page: GithubscorePage;

  beforeEach(() => {
    page = new GithubscorePage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
