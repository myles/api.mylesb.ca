import Relay from 'react-relay';

export default class extends Relay.Route {
  static queries = {
    about: () => Relay.QL`
      query {
        about
      }
    `,
  };

  static routeName = 'Route';
}
