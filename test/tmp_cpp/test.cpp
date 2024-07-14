int LedNameSpace::handle(const std::vector<std::string>& messages, const int data, const LedBase& base) {
    if (data != 255) {
        auto it = _ledMap.find(data);
        if (it != _ledMap.end()) {
            displayText(F_IP, base, it->second, true);
            displayText(R_IP, base, it->second, true);
        } else {
            displayPicture(F_IP, base, data);
            displayPicture(R_IP, base, data);
        }
    } else {
        if (messages.empty()) {
            logger(Color::RED, getCurrentDateTime(), "No message provided, cleaning all areas.");
            cleanAllAreaProgram();
        } else {
            const auto& message = messages[base.Id];
            if (message.empty()) {
                cleanAreaProgram(base.Id);
            } else {
                displayText(F_IP, base, message, true);
                displayText(R_IP, base, message, true);
            }
        }
    }
    return 0;
}