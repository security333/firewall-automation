#!/bin/bash

# Function to display the menu
show_menu() {
    echo "================================="
    echo " Network Tools Menu"
    echo "================================="
    echo "1. Display IPv4 routing table (ip route)"
    echo "2. Display IPv6 routing table (ip -6 route)"
    echo "3. Display IPv4 routing table (netstat -r)"
    echo "4. Display IPv6 routing table (netstat -r -6)"
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
            if command -v ip &>/dev/null; then
                ip -4 route
            else
                echo "Error: 'ip' command not found."
            fi
            ;;
        2)
            echo "IPv6 Routing Table (ip -6 route):"
            if command -v ip &>/dev/null; then
                ip -6 route
            else
                echo "Error: 'ip' command not found."
            fi
            ;;
        3)
            echo "IPv4 Routing Table (netstat -r):"
            if command -v netstat &>/dev/null; then
                netstat -r -4
            else
                echo "Error: 'netstat' command not found. Please install 'net-tools'."
            fi
            ;;
        4)
            echo "IPv6 Routing Table (netstat -r -6):"
            if command -v netstat &>/dev/null; then
                netstat -r -6
            else
                echo "Error: 'netstat' command not found. Please install 'net-tools'."
            fi
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
