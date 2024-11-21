#!/bin/bash

# Function to display the menu
show_menu() {
    echo "================================="
    echo " Network Tools Menu"
    echo "================================="
    echo "1. Display IPv4 routing table (ip route)"
    echo "2. Display IPv6 routing table (ip -6 route)"
    echo "3. Display IPv4 routing table (netstat -r)"
    echo "4. Display IPv6 routing table (netstat -r)"
    echo "5. Exit"
    echo "================================="
}

# Infinite loop for menu selection
while true; do
    show_menu
    read -p "Enter your choice [1-5]: " choice

    case $choice in
        1)
            echo "IPv4 Routing Table (ip route):"
            ip route
            ;;
        2)
            echo "IPv6 Routing Table (ip -6 route):"
            ip -6 route
            ;;
        3)
            echo "IPv4 Routing Table (netstat -r):"
            netstat -r -4
            ;;
        4)
            echo "IPv6 Routing Table (netstat -r):"
            netstat -r -6
            ;;
        5)
            echo "Exiting the menu. Goodbye!"
            break
            ;;
        *)
            echo "Invalid choice. Please select a valid option."
            ;;
    esac

    echo ""
done
