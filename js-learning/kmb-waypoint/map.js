//CSS Change with img
const waypoint = document.querySelector(".waypoint");
const popup = document.querySelector('.popup');
function handleMouseEnterWaypoint() {
  waypoint.className = "waypointActive";
  popup.className ="popupActive";
}
function handleMouseLeaveWaypoint() {
  waypoint.className = "waypoint";
  popup.className ="popup";
}

waypoint.addEventListener("mouseenter", handleMouseEnterWaypoint);
waypoint.addEventListener("mouseleave", handleMouseLeaveWaypoint);
popup.addEventListener("mouseenter", handleMouseEnterWaypoint);
popup.addEventListener("mouseleave", handleMouseLeaveWaypoint);
// popupActive.addEventListener("mouseover", handleMouseEnterWaypoint);
