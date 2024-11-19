export default function NeighborhoodManager() {
    this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];
  
    // Method to add a new neighborhood
    this.addNeighborhood = (newNeighborhood) => {
      if (newNeighborhood && !this.sanFranciscoNeighborhoods.includes(newNeighborhood)) {
        this.sanFranciscoNeighborhoods.push(newNeighborhood);
      }
      return this.sanFranciscoNeighborhoods;
    };
  
    // Method to get the list of neighborhoods
    this.getNeighborhoodsList = () => {
      return this.sanFranciscoNeighborhoods;
    };
  }
